# Fake Review Detection Project

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Chrome Extension](#chrome-extension)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Fake Review Detection Project is designed to identify fake reviews on Amazon using a Long Short-Term Memory (LSTM) model. The project achieves an impressive accuracy of 98%. Additionally, a Chrome extension is provided to detect fake reviews directly on Amazon product pages.

## Features

- **LSTM Model**: Detects fake reviews with 98% accuracy.
- **Chrome Extension**: Real-time detection of fake reviews on Amazon product pages.
- **User-Friendly Interface**: Easy to use for end-users.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Node.js and npm (for Chrome extension development)

### Clone the Repository

```bash
git clone https://github.com/sameer-quresh/MACHINE-LEARNING-PROJECT.git
cd MACHINE-LEARNING-PROJECT
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python train_model.py



Results
The LSTM model achieved an accuracy of 98% on the test dataset, demonstrating its effectiveness in detecting fake reviews.
