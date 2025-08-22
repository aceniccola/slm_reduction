import os
import json
import requests
import polars as pl
import langchain_community
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chains import RetrievalQA
import streamlit as st
import torch
from dotenv import load_dotenv

# creating a rag pipeline
load_dotenv()

def get_data(url):
    response = requests.get(url)
    return response.json()

def get_data_from_file(file_path):
    with open(file_path, 'r') as file: