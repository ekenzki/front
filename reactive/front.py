from charmhelpers.core.hookenv import status_set, log
from charms.reactive import when, when_not, set_state, endpoint_from_flag

@when_not('endpoint.backend.joined')
def not_ready_yet():
    status_set('blocked', 'Missing backend relation')

@when('endpoint.backend.new-signal')
def is_backend_connected():
    log("We got a signal from the backend")
    backend = endpoint_from_flag('endpoint.backend.new-signal')
    if backend.are_backends_ready():
        status_set('active', 'Ready')
    else:
        status_set('waiting', 'Waiting for backends to come online')
