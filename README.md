# YOLO_cell

# Prediction Application

This application is designed to assist in the identification of cows suffering from subclinical endometritis by calculating the percentage of polymorphonuclear cells. Users can upload images, which are then predicted by the YOLO model to provide insights into the health of the cow based on cell counts.

## Requirements

- Streamlit
- PIL (Python Imaging Library)
- ultralytics (for the YOLO model)
- re (for regex operations)

## How to Run

1. The application is hosted and available at [https://yolocell.streamlit.app/](https://yolocell.streamlit.app/). You can access and use it directly from this link.
2. If you wish to run it locally, start by cloning the repository.

  
## Features

- **Load Model**: The application loads a pre-trained YOLO model from the `model.pt` file.
- **Predict Images**: Users can upload images which are then predicted by the model.
- **Display Results**: The application displays the predicted image along with information on the count of "polis" and "monos" cells, as well as the percentage of polymorphonuclear cells.

## Contact

If you have questions or suggestions regarding this application, please contact dawid.tobolski@uwm.edu.pl or tobola28@gmail.com.
