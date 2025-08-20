import os
import json
import requests
import pandas as pd
import langchain_community
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chains import RetrievalQA
from langchain_community.prompts import PromptTemplate
import streamlit as st
import torch
from dotenv import load_dotenv

load_dotenv()


def get_data(url):
    response = requests.get(url)
    return response.json()


def get_data_from_file(file_path):
    with open(file_path, 'r') as file: