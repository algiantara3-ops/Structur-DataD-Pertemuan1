{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/algiantara3-ops/Structur-DataD-Pertemuan1/blob/main/latihan%20percobaan.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Wf5KrEb6vrkR"
      },
      "source": [
        "# Selamat Datang di Colab!"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "JQesyTg7QSU-"
      },
      "outputs": [],
      "source": [
        "from google.colab import ai\n",
        "response = ai.generate_text(\"What is the capital of France?\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "arr= np.array([10,20,30,40,50])\n",
        "print (arr)"
      ],
      "metadata": {
        "id": "oBNEFOBs31hJ",
        "outputId": "d6dc686f-9032-4b39-c2dc-f04a80578a1d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[10 20 30 40 50]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#import as numpy untuk bekerja dengan array\n",
        "import numpy as np\n"
      ],
      "metadata": {
        "id": "WC2x9Sc84ncI"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# array berisi 10 bilangan ganjil\n",
        "print (\"1. array berisi bilangan ganjil\")\n",
        "# membuat array bilangan ganjil pertama\n",
        "x= np.array([1,2,3,4,5,6,7,8,9,10])\n",
        "print(x)"
      ],
      "metadata": {
        "id": "7sZlBSTw4570",
        "outputId": "22598f4d-402e-4293-ab78-9cb51d23bc4d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1. array berisi bilangan ganjil\n",
            "[ 1  2  3  4  5  6  7  8  9 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# mencari nilai tertinggi\n",
        "print (\"2. nilai tertingggi\")\n",
        "x= np.array([1,2,3,4,5,6,7,8,9,10])\n",
        "\n",
        "nilai_tertinggi = np.max(x)\n",
        "print(x)\n",
        "print (\"x\", nilai_tertinggi)"
      ],
      "metadata": {
        "id": "J0UmZQQu5vik",
        "outputId": "7c570d34-ccf9-4ecf-d6de-fe945961b8b2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2. nilai tertingggi\n",
            "[ 1  2  3  4  5  6  7  8  9 10]\n",
            "x 10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# mencri nilai terendah\n",
        "print(\"3.nilai terendah\")\n",
        "x= np.array([1,2,3,4,5,6,7,8,9,10])\n",
        "nilai_terendah = np.min(x)\n",
        "print(x)\n",
        "print(\"x\", nilai_terendah)"
      ],
      "metadata": {
        "id": "TZAHbfCx7I9k",
        "outputId": "679fdb91-268a-42d9-ead8-76857b7ec425",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.nilai terendah\n",
            "[ 1  2  3  4  5  6  7  8  9 10]\n",
            "x 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# mencari rata-rata\n",
        "print(\"4.rata-rata\")\n",
        "x= np.array ([1,2,3,4,5,6,7,8,9,10])\n",
        "rata_rata = np.mean(x)\n",
        "print(x)\n",
        "print(\"x\", rata_rata)\n",
        "#"
      ],
      "metadata": {
        "id": "eTBgK37t8rb0",
        "outputId": "c9f30a11-b304-4e1e-ee50-d4f60651dc98",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4.rata-rata\n",
            "[ 1  2  3  4  5  6  7  8  9 10]\n",
            "x 5.5\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}