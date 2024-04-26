import time

from skywalking.agent import SkyWalkingAgent
from skywalking import agent, config
from skywalking import agent
from skywalking.trace.tags import Tag
from skywalking.trace.context import SpanContext

config.agent_collector_backend_services = '127.0.0.1:11800'
config.agent_name = 'test'

agent.start()

context = SpanContext()

with context.new_entry_span('operation_name') as span:
    tag = Tag("标签值")
    span.tag(tag)
    time.sleep(1.5)
