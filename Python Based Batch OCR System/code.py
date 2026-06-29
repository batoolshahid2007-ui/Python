import os


class BatchOCRSystem:

    def __init__(self, imagefolder="images", textfolder="outputtext"):
        self.imagefolder = imagefolder
        self.textfolder = textfolder

        if not os.path.exists(self.imagefolder):
            os.makedirs(self.imagefolder, exist_ok=True)
            print(
                f"[INFO] Created '{self.imagefolder}' directory. Please place your images here."
            )

        if not os.path.exists(self.textfolder):
            os.makedirs(self.textfolder, exist_ok=True)
            print(
                f"[INFO] Created '{self.textfolder}' directory for saving results."
            )

    def preprocess_image(self, imagename):
        return f"{imagename} is preprocessed (grayscale, noise reduced, threshold applied)"

    def perform_ocr(self, processed_data):
        return f"OCR result for {processed_data} : This is simulated extracted text"

    def save_text(self, imagename, text):
        base_name, _ = os.path.splitext(imagename)
        filename = base_name + ".txt"
        filepath = os.path.join(self.textfolder, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text)

    def batch_process(self):
        if not os.listdir(self.imagefolder):
            print(f"Folder Status: '{self.imagefolder}' is currently empty.")
            print(
                f"Action Required: Drop some .jpg, .jpeg, or .png files into the '{self.imagefolder}' folder and re-run."
            )
            return

        files = os.listdir(self.imagefolder)
        processed_count = 0

        print(f"Scanning '{self.imagefolder}' for images...")

        for name in files:
            if name.lower().endswith((".jpg", ".jpeg", ".png")):
                processed = self.preprocess_image(name)
                text = self.perform_ocr(processed)
                self.save_text(name, text)
                print(f"Processed: {name} => Text saved successfully.")
                processed_count += 1

        if processed_count > 0:
            print(
                f"Success: All {processed_count} images processed. Results are in '{self.textfolder}'."
            )
        else:
            print(
                f"Warning: No valid image formats found in '{self.imagefolder}'. Supported: .jpg, .jpeg, .png"
            )


if __name__ == "__main__":
    images_dir = "images"
    output_dir = "outputtext"

    ocr_system = BatchOCRSystem(imagefolder=images_dir, textfolder=output_dir)
    ocr_system.batch_process()
