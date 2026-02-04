from .base_stage import PipelineStage
from .data_types import TextFile


class DummyStage(PipelineStage):
    name = "DummyStage"
    inputs = [("numbers", TextFile)]
    outputs = [("new_numbers", TextFile)]
    config_options = {"multiplier": float}

    def run(self):
        # Retrieve configuration:
        my_config = self.config
        print("Here is my configuration :", my_config)

        for inp, _ in self.inputs:
            filename = self.get_input(inp)
            print(f"    numbers reading from {filename}")
            with open(filename) as f:
                numbers = [float(line.strip()) for line in f]

        for out, _ in self.outputs:
            filename = self.get_output(out)
            print(f"    new_numbers writing to {filename}")
            with open(filename, "w") as f:
                for n in numbers:
                    f.write(f"{n * my_config['multiplier']}\n")
