from .base_stage import PipelineStage
from .data_types import TextFile

from time import sleep

import numpy as np


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


class DummyStageWait(PipelineStage):
    name = "DummyStageWait"
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

        np.random.seed(int(numbers[0]))  # Seed the random number generator for reproducibility
        sleep_time = np.random.uniform(10, 20)
        print(f"Sleeping for {sleep_time:.1f} seconds...")
        sleep(sleep_time)

        for out, _ in self.outputs:
            filename = self.get_output(out)
            print(f"    new_numbers writing to {filename}")
            with open(filename, "w") as f:
                for n in numbers:
                    f.write(f"{n * my_config['multiplier']}\n")


class DummyStageWait2(PipelineStage):
    name = "DummyStageWait2"
    inputs = [("numbers", TextFile), ("new_numbers", TextFile)]
    outputs = [("new_numbers2", TextFile)]
    config_options = {"multiplier": float}

    def run(self):
        # Retrieve configuration:
        my_config = self.config
        print("Here is my configuration :", my_config)

        filename = self.get_input("numbers")
        print(f"    numbers reading from {filename}")
        with open(filename) as f:
            numbers = [float(line.strip()) for line in f]

        filename = self.get_input("new_numbers")
        print(f"    new_numbers reading from {filename}")
        with open(filename) as f:
            new_numbers = [float(line.strip()) for line in f]

        np.random.seed(int(new_numbers[0]))  # Seed the random number generator for reproducibility
        sleep_time = np.random.uniform(10, 20)
        print(f"Sleeping for {sleep_time:.1f} seconds...")
        sleep(sleep_time)

        for out, _ in self.outputs:
            filename = self.get_output(out)
            print(f"    new_numbers writing to {filename}")
            with open(filename, "w") as f:
                for i in range(len(numbers)):
                    f.write(f"{(new_numbers[i] + numbers[i]) * my_config['multiplier']}\n")
