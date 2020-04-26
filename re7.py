import logging

from .engine_functions import _engine_proxy
from tng.frontend.global_engine import get_engine, device_type_map
from tng.device_helpers.addresses import create_addrs_from_str_if_required
from tng.device_helpers.device_factory import CreateDeviceError

log = logging.getLogger('tng.api')


def interface(name, version):
    '''Decorator to register an interface class for a version

    :param name: The name of the interface type. E.g. 'cuil' or 'intouch'
    :param version: The version this interface is valid for. E.g. 'TC6'
    '''
    def decorator(cls):
        get_engine().device_factory.interface(name, version, cls)
        return cls
    return decorator


def create_device(
        hostname, device_type=None, name=None, target=None,
        engine=_engine_proxy, **kwargs):
    '''Creates a new TNG Pi :class:`~tng.device.abc_device.ABCDevice` given a
    hostname/IP, optional device type and setup parameters. If no device type
    is specified TNG Pi will probe the device to determine it's device type. If
    a device with the given hostname has already been created, TNG will be lazy
    and return a refernce to the pre-existing device. To force recreation of  a
    device, use ``tng.api.recreate_device``.

    :parameter hostname: hostname/IP/DeviceAddrs of device
    :parameter device_type: type of device to create, e.g. ``'saturn'``
        (default: ``None``)
    :parameter name: sym name for device, e.g. ``'epa'`` (default: ``None``)
    :parameter target: is this device a target (default: ``False``)
    :parameter engine: an instance of TNG's core engine (used primarily for
        unit testing)
    :parameter kwargs: optional setup parameters, e.g. password='x'

    .. rubric:: Setup

    Setup parameters are passed via ``**kwargs`` and are used during probing
    and passed to the device on construction. Known parameters include:

    * username - username to use during CUIL access (default: ``'admin'``)
    * password - password to use in CUIL access (default: ``''``)
    * rootpassword - password for the root user for SSH (default: ``''``)

    See the constructor of each device for the full set of setup parameters
    supported by the device.

    .. rubric:: CUIL Probe

    For the CUIL probe TNG Pi attempts to read */Status/SystemUnit* via HTTP
    (ports 80, 8080 and 8091). The device type then is inferred from the
    `Product`, `ProductId` or `ProductPlatform` subelements. If the CUIL
    requires authentication make sure to specify the `password` setup
    parameter, and also `username` if the user is not "admin".

    .. rubric:: Examples

    To create a VCS device (assuming passwords are 'x'):

    >>> self.vcs = tng.create_device('10.50.157.213', password='x',
    ...     rootpassword='x')

    To create a C90 device:

    >>> self.epa = tng.create_device('10.50.158.81')
    '''
    addrs = create_addrs_from_str_if_required(hostname)
    device = engine.device_factory.get_or_create_device(
        addrs, device_type=device_type, name=name, target=target,
        **kwargs)
    return device


def create_devices(
        devices, defaults=None, engine=_engine_proxy, fail_fast=True):
    '''Creates a set of TNG Pi devices in parallel.

    Devices may be specified via a list or dictionary mapping device names
    to devices. Each device is then specified as a hostname/IP or
    device info dictionary (containing device options/setup). See above
    for device options/setup.

    Default device options/setup may be provided via option `defaults`.

    :parameter devices: list or dict of device descriptions
    :parameter defaults: device options common to all devices that are not
        provided in the description
        (default: ``None``)
    :parameter engine: an instance of TNG's core engine (used primarily for
        unit testing)
    :parameter fail_fast: if ``False``, replace devices that could not be
        created with ``None`` in the returned devices list instead of raising
        the exception
        (default: ``True``)

    :returns: A list of the created devices.

    .. rubric:: Specifying Device Descriptions

    For example, to create two devices from IPs using default password 'x':

    >>> create_devices(['10.50.158.98','10.50.158.99'],
    ...     defaults=dict(password='x'))

    To give the devices meaningful names, use a dictionary:

    >>> create_devices(dict(epa='10.50.158.98', epb='10.50.158.99'),
    ...     defaults=dict(password='x'))

    Alternatively, device info can be specified in full per device:

    >>> create_devices(dict(
    ...     epa=dict(uri='10.50.158.98',target=True,type='C20'),
    ...     epb='10.50.158.99'),
    ...     defaults=dict(password='x'))


    .. note::
        Devices may be a list of device addresses, or a dictionary mapping
        names to device info.

        In addition, we need to map uri/ip/hostname => addrs and type =>
        device_type.
    '''
    device_specs = []
    # convert list/dict to (name, dict) tuples
    if isinstance(devices, dict):
        items = devices.items()
    else:
        items = [(None, d) for d in devices]

    for (device_name, device_info) in items:
        device_spec = {}
        if defaults:
            device_spec.update(defaults)
        if isinstance(device_info, dict):
            for k, v in device_info.items():
                if k in ('uri', 'ip'):
                    device_spec['addrs'] = create_addrs_from_str_if_required(v)
                elif k == 'type':
                    device_spec['device_type'] = v
                else:
                    device_spec[k] = v
            # check that device has addrs defined - if not the call to
            # create_device() will fail strangely
            if 'addrs' not in device_spec:
                if device_name is None:
                    device = repr(device_info)
                else:
                    device = '%r (%r)' % (device_name, device_info)
                raise CreateDeviceError(
                    'Cannot create device %s, please specify some kind of '
                    'address.' % device)
            else:
                device_spec['addrs'] = create_addrs_from_str_if_required(
                    device_spec['addrs'])
        else:
            device_spec['addrs'] = create_addrs_from_str_if_required(
                device_info)
        if device_name is not None:
            device_spec['name'] = device_name
        device_specs.append(device_spec)

    create_devices_ = engine.device_factory.create_devices
    devs = create_devices_(device_specs, fail_fast=fail_fast)
    return devs


def recreate_device(
        hostname, name=None, target=None, device_type=None,
        engine=_engine_proxy, **kwargs):
    '''Forces TNG to recreate a device as if it never knew about it. This will
    replace any existing device object with a new object and your old
    references will become stale. You should use this is situations where the
    old object has become unusable - for example, if you have upgraded the
    software on a device.

    :parameter engine: an instance of TNG's core engine (used primarily for
        unit testing)
    '''
    addrs = create_addrs_from_str_if_required(hostname)
    existing_device = engine.device_factory.get_device_with_addr(addrs)
    if existing_device:
        engine.device_factory.cleanup_device(existing_device)
    else:
        raise ValueError('No devices found for {!r}'.format(addrs))
    device = engine.device_factory.create_device(
        addrs, device_type=device_type, name=name, target=target,
        **kwargs)
    return device


def get_system(name, engine=get_engine()):
    '''Gets a TNG pi :class:`~tng.device.abc_device.ABCDevice` by setup file
    name, or raises :class:`KeyError` if not found.

    >>> get_system("vcs")
    <ABCDevice Oak 10.50.156.80>

    .. seealso:: :meth:`~tng.device.abc_device.ABCDevice.name`
    '''
    for system in get_systems(engine):
        if system.name == name:
            return system
    raise KeyError('No system with name %s found' % name)


def get_systems(engine=get_engine()):
    '''Returns all the :class:`~tng.device.abc_device.ABCDevice` that TNG pi
    has created.

    They are loosely ordered in that all targets come first, then all refs.
    '''
    return get_targets(engine) + get_refeps(engine)


def _get_systems(engine=get_engine()):
    return list(engine.device_factory.devices)


def get_targets(engine=get_engine()):
    '''Returns all the :class:`~tng.device.abc_device.ABCDevice` objects for
    which is_target() returns True.
    '''
    return [system for system in _get_systems(engine) if system.is_target()]


def get_refeps(engine=get_engine()):
    '''Returns all the :class:`~tng.device.abc_device.ABCDevice` objects for
    which is_target() returns False.'''
    return [
        system for system in _get_systems(engine) if not system.is_target()]


def creatable_device(*names):
    '''Class decorator used to map a name to an
    :class:`tng.device.abc_device.ABCDevice` class in |tng|'s engine.  The name
    used can be passed as the ``device_type`` argument to
    :meth:`tng.api.create_device`, which will the resolve to the decorated
    class during device creation.

    :parameters str's names: the names to bind the Device class to.

    If no names are given, it defaults to lower case of the class
        name.
    '''
    return device_type_map(*names)


def list_device_types(engine=_engine_proxy):
    '''Lists the names of the types of devices that have been registered in
    this running instance of |tng|. Any of these can be passed as the
    ``device_type`` argument to :meth:`tng.api.create_device` to skip |tng|'s
    device probing mechanism and force-create a known device.

    :parameter engine: The :class:`tng.frontend.engine.Engine` instance on
        which device name registration should be checked. The default is
        completely sufficient for all normal usage, but can be overridden for
        unit testing.
    :returns: an alphabetically ordered list of registered names for device
        type definitions that |tng| knows about.

    .. warning::
        This API is useful for device authors testing their code, but should
        not be considered useful practice for day-to-day testing.
    '''
    return sorted(engine.device_factory.device_names)