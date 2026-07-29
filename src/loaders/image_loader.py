from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


class ImageLoader:
    _processor = None
    _model = None

    def __init__(self):
        if ImageLoader._processor is None:
            ImageLoader._processor = BlipProcessor.from_pretrained(
                "Salesforce/blip-image-captioning-base"
            )

        if ImageLoader._model is None:
            ImageLoader._model = BlipForConditionalGeneration.from_pretrained(
                "Salesforce/blip-image-captioning-base"
            )

        self.processor = ImageLoader._processor
        self.model = ImageLoader._model

    def generate_caption(self, image) -> str:
        if not isinstance(image, Image.Image):
            image = Image.open(image).convert("RGB")

        inputs = self.processor(images=image, return_tensors="pt")

        output = self.model.generate(**inputs)

        caption = self.processor.decode(
            output[0],
            skip_special_tokens=True,
        )

        return caption