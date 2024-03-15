FROM python:3.8
WORKDIR /main
COPY . /main
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["streamlit","run", "main.py"]
