from faker import Faker

fake = Faker()

class TuberculosisAnalyzer:
    def __init__(self):
        self.ml_data = []
        self.model_used = "CIH dataset"
        self.data_set_name = "Tuberculosis Dataset"
        self.libraries_used = ["scikit-learn", "pandas", "numpy"]

    def generate_ml_data(self, num_samples=10):
        for _ in range(num_samples):
            age = fake.random_int(1, 100)
            symptoms = fake.words(nb=3)
            result = fake.random_element(elements=("Positive", "Negative"))
            self.ml_data.append({
                "age": age,
                "symptoms": symptoms,
                "result": result
            })

    def print_model_info(self):
        print("Model used:", self.model_used)
        print("Name of dataset:", self.data_set_name)
        print("Libraries used:", ', '.join(self.libraries_used))
        print("Model started at http://tb.test.woza.work/ or localhost at 127.0.0.1")

    def get_model_info(self):
        model_info = {
            "Model used": self.model_used,
            "Name of dataset": self.data_set_name,
            "Libraries used": self.libraries_used,
            "Link": "http://tb.test.woza.work/ or localhost at 127.0.0.1"
        }
        return model_info

def print_logs():
    logs = [
        "9.9s\t1\t[NbConvertApp] Converting notebook script.ipynb to html",
        "14.6s\t2\t[NbConvertApp] Executing notebook with kernel: python3",
        "300.5s\t3\t2018-11-24 12:28:31.150016: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:964] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero",
        "300.5s\t4\t2018-11-24 12:28:31.152618: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1411] Found device 0 with properties:",
        "name: Tesla K80 major: 3 minor: 7 memoryClockRate(GHz): 0.8235",
        "pciBusID: 0000:00:04.0",
        "totalMemory: 11.17GiB freeMemory: 11.10GiB",
        "2018-11-24 12:28:31.152652: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1490] Adding visible gpu devices: 0",
        "301.6s\t5\t2018-11-24 12:28:32.314264: I tensorflow/core/common_runtime/gpu/gpu_device.cc:971] Device interconnect StreamExecutor with strength 1 edge matrix:",
        "2018-11-24 12:28:32.314333: I tensorflow/core/common_runtime/gpu/gpu_device.cc:977]      0",
        "2018-11-24 12:28:32.314345: I tensorflow/core/common_runtime/gpu/gpu_device.cc:990] 0:   N",
        "2018-11-24 12:28:32.314651: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1103] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 10758 MB memory) -> physical GPU (device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7)",
        "623.8s\t6\t[NbConvertApp] Support files will be in __results___files/",
        "[NbConvertApp] Making directory __results___files",
        "623.8s\t7\t[NbConvertApp] Making directory __results___files",
        "[NbConvertApp] Making directory __results___files",
        "[NbConvertApp] Making directory __results___files",
        "[NbConvertApp] Making directory __results___files",
        "[NbConvertApp] Making directory __results___files",
        "[NbConvertApp] Writing 452274 bytes to __results__.html"
    ]

    print("Time\t#\tLog Message")
    for log in logs:
        print(log)

    print("\nLink: started at http://tb.test.woza.work/")

if __name__ == "__main__":
    analyzer = TuberculosisAnalyzer()
    analyzer.generate_ml_data()
    model_info = analyzer.get_model_info()
    print("Generated Machine Learning Data:")
    print(analyzer.ml_data)
    print("\nModel Information:")
    for key, value in model_info.items():
        if key == "Libraries used":
            print(f"{key}:")
            for lib in value:
                print(f"- {lib}")
        else:
            print(f"{key}: {value}")

    print_logs()
