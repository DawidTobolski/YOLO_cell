import streamlit as st
import os
from PIL import Image
from ultralytics import YOLO
import re

# Wczytaj model
model = YOLO("model.pt")

# Ustal ścieżkę dla wyników
output_dir = 'temp_out_res'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Funkcja do przewidywania obrazów
def predict_image(image_path):
    results = model.predict(source=image_path)
    input_filename = os.path.basename(results[0].path)
    annotated_img = results[0].plot()
    pil_image = Image.fromarray(annotated_img[..., ::-1])
    pil_image.save(os.path.join(output_dir, input_filename))
    
    total_polis = 0
    total_monos = 0
    polis_index = 0
    monos_index = 1
    verbose_output = results[0].verbose()
    
    polis_match = re.search(r'(\d+) poli', verbose_output)
    monos_match = re.search(r'(\d+) mono', verbose_output)
    
    if polis_match:
        total_polis += int(polis_match.group(1))
    if monos_match:
        total_monos += int(monos_match.group(1))

    if total_polis + total_monos == 0:
        polis_percentage = 0
    else:
        polis_percentage = (total_polis / (total_polis + total_monos)) * 100

    return os.path.join(output_dir, input_filename), total_polis, total_monos, polis_percentage

# Główna funkcja Streamlit
def main():
    st.title("YOLO Predykcja")

    uploaded_file = st.file_uploader("Wybierz obraz do przewidzenia", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image_path = os.path.join(output_dir, uploaded_file.name)
        with open(image_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        st.image(image_path, caption='Wczytane zdjęcie.', use_column_width=True)
        
        if st.button("Przewiduj"):
            pred_img_path, polis_count, monos_count, polis_perc = predict_image(image_path)
            st.image(pred_img_path, caption='Przewidziane zdjęcie.', use_column_width=True)
            st.write(f"Łączna liczba komórek 'polis': {polis_count}")
            st.write(f"Łączna liczba komórek 'monos': {monos_count}")
            st.write(f"Procent komórek polimorfonuklearnych: {polis_perc:.2f}%")

if __name__ == '__main__':
    main()
