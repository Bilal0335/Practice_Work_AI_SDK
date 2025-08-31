
# ! tracing_agent.py

from agents import Agent,set_tracing_disabled,set_trace_processors
from agents.tracing.processors import ConsoleSpanExporter,BatchTraceProcessor,default_processor
from agents.tracing.processor_interface import TracingExporter
from agents.tracing.spans import Span
from agents.tracing.traces import Trace
from my_config.gemini_config import GEMINI_MODEL

import rich

class CustomConsoleSpanExporter(TracingExporter):
    def export(self, items: list[Trace | Span]):
        for item in items:
            if isinstance(item, Trace):
                print(f"[Trace] ID: {item.trace_id} | Name: {item.name}")
            elif item.span_data.type == "generation":
                usage = item.span_data.usage or {}
                model = item.span_data.model
                user_input = item.span_data.input or []
                output = item.span_data.output or []

                print("🧠 Model Used:", model)
                print("📥 Input Tokens:", usage.get("input_tokens", "N/A"))
                print("📤 Output Tokens:", usage.get("output_tokens", "N/A"))

                if user_input:
                    print("🙋 User Asked:", user_input[-1].get("content", "N/A"))
                if output:
                    print("🤖 Bot Replied:", output[0].get("content", "N/A"))


# expoter = ConsoleSpanExporter()
exporter = CustomConsoleSpanExporter()
processor = BatchTraceProcessor(exporter)



# set_tracing_disabled(disabled=True)
set_trace_processors([
                      processor,
                    #   default_processor()  # sent to the dashbaord openai
                      ]) # override default processor(s)

tracing_agents = Agent(
    name="my_agent",
    instructions="You are helpfull assistant.",
    model=GEMINI_MODEL
)