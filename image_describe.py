from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import sys

model_id = "vikhyatk/moondream2"
revision = "2024-07-23"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

image = Image.open(sys.argv[1])
enc_image = model.encode_image(image)
print(model.answer_question(enc_image, "Describe this image.", tokenizer))
