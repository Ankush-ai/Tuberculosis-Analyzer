from faker import Faker
import requests

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
    