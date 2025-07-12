# Multitemporal Satellite Change Detection

A deep learning project for multitemporal satellite change detection using computer vision techniques and GPU acceleration.

## Overview

This project implements satellite image analysis algorithms to detect changes between satellite images taken at different times. The implementation focuses on identifying various types of changes such as urban development, deforestation, natural disasters, and other environmental modifications using deep learning approaches.

🔗 **[View the complete implementation on Kaggle](https://www.kaggle.com/code/saverino/multitemporal-satellite-change-detection)**

## Quick Start

You can directly run the code on Kaggle for the best experience:

- **Notebook link**: [Kaggle Notebook](https://www.kaggle.com/code/saverino/multitemporal-satellite-change-detection)
- **Hardware**: Go to *Settings → Accelerator* and select **GPU T4 x2** for GPU-accelerated computation.

### Dataset Links

- [LEVIR-CD Change Detection Dataset](https://www.kaggle.com/datasets/mdrifaturrahman33/levir-cd)
- [Project Notebook (for code and sample data)](https://www.kaggle.com/code/saverino/multitemporal-satellite-change-detection)
- [Sample Flowchart Images](https://www.kaggle.com/datasets/saverino/flow-chart-image)

> The code and datasets are also uploaded within this repository in case there are issues accessing Kaggle directly.

## Features

- **Multitemporal Analysis**: Compare satellite images across different time periods.
- **Deep Learning Models**: GPU-accelerated neural networks for change detection.
- **Image Processing**: Advanced preprocessing techniques for satellite imagery.
- **Change Visualization**: Visual representation of detected changes.
- **Performance Optimization**: GPU-optimized implementations for faster processing.

## Technology Stack

- **Python**: Primary programming language
- **Jupyter Notebook**: Interactive development environment
- **GPU Computing**: CUDA-enabled deep learning frameworks
- **Computer Vision Libraries**: OpenCV, PIL for image processing
- **Deep Learning**: TensorFlow/PyTorch with GPU acceleration
- **Geospatial Libraries**: For handling satellite imagery data

## Repository Structure

```
Multitemporal-Satellite-Change-Detection/
├── multitemporal-satellite-change-detection.ipynb  # Main notebook implementation
├── README.md                                       # Project documentation
└── LICENSE                                         # Apache 2.0 License
```

## Requirements

### Hardware
- **GPU Required**: NVIDIA GPU with CUDA support recommended for optimal performance
- **RAM**: Minimum 8GB, 16GB+ recommended for larger datasets
- **Storage**: Sufficient space for satellite imagery datasets

### Software
- Python 3.7+
- CUDA toolkit (for GPU acceleration)
- Jupyter Notebook
- Required Python packages as specified in the notebook

## Getting Started

### Option 1: Run on Kaggle (Recommended)
1. Visit the [Kaggle notebook](https://www.kaggle.com/code/saverino/multitemporal-satellite-change-detection)
2. Fork the notebook to your Kaggle account
3. Enable GPU acceleration in Kaggle settings (GPU T4 x2)
4. Run all cells

### Option 2: Local Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/saverin0/Multitemporal-Satellite-Change-Detection.git
    cd Multitemporal-Satellite-Change-Detection
    ```
2. Ensure CUDA and GPU drivers are properly installed
3. Open the notebook:
    ```bash
    jupyter notebook multitemporal-satellite-change-detection.ipynb
    ```

## Usage

The notebook provides a complete pipeline for:
1. **Data Loading**: Import and preprocess satellite image pairs
2. **Model Architecture**: Define deep learning models optimized for change detection
3. **Training**: GPU-accelerated model training
4. **Inference**: Apply trained models to detect changes
5. **Visualization**: Display results with change maps and statistics

## Performance Notes

- **GPU Acceleration**: The implementation is optimized for GPU computing
- **Memory Management**: Efficient handling of large satellite imagery datasets
- **Batch Processing**: Support for processing multiple image pairs

## Applications

- **Urban Planning**: Monitor urban expansion and infrastructure development
- **Environmental Monitoring**: Track deforestation, land use changes, and habitat loss
- **Disaster Assessment**: Evaluate damage from natural disasters
- **Agriculture**: Monitor crop changes and agricultural patterns
- **Climate Research**: Study long-term environmental changes

## References

- Urban Change Detection for Multispectral Earth Observation Using Convolutional Neural Networks, R. Caye Daudt, B. Le Saux, A. Boulch, Y. Gousseau.  
  IEEE International Geoscience and Remote Sensing Symposium (IGARSS’2018), Valencia, Spain, July 2018.  
  [OSCD ONERA Satellite Change Detection Dataset](https://ieee-dataport.org/open-access/oscd-onera-satellite-change-detection)

- Multitemporal Satellite Change Detection  
  Author: Saverino, kshitij2602  
  Kaggle: https://www.kaggle.com/code/saverino/multitemporal-satellite-change-detection  
  GitHub: https://github.com/saverin0/Multitemporal-Satellite-Change-Detection

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for discussions.

---

*This project demonstrates the application of deep learning and GPU computing for satellite imagery analysis and environmental monitoring.*
