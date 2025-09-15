import os
import shutil
import zipfile
from typing import List
from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import FileResponse
from services.pdf_service import clean_pdf

router = APIRouter(prefix="/api")  # tất cả route đều bắt đầu bằng /api

@router.post("/pdf/single")
async def single_process(file: UploadFile, mode: str = Form("mask")):
    """
    Xử lý một file PDF: che hoặc xóa số điện thoại & email
    """
    os.makedirs("temp", exist_ok=True)
    input_path = f"temp/{file.filename}"
    output_path = f"temp/cleaned_{file.filename}"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    clean_pdf(input_path, output_path, mode)
    return FileResponse(output_path, filename=f"cleaned_{file.filename}")


@router.post("/pdf/multi")
async def multi_process(files: List[UploadFile], mode: str = Form("mask")):
    """
    Xử lý nhiều file PDF cùng lúc (trả về file ZIP)
    """
    os.makedirs("temp", exist_ok=True)
    result_files = []

    for file in files:
        input_path = f"temp/{file.filename}"
        output_path = f"temp/cleaned_{file.filename}"

        with open(input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        clean_pdf(input_path, output_path, mode)
        result_files.append(output_path)

    # Tạo file ZIP chứa kết quả
    zip_path = "result/processed_files.zip"
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file_path in result_files:
            zipf.write(file_path, os.path.basename(file_path))

    return FileResponse(zip_path, filename="processed_files.zip")


@router.get("/status")
async def status():
    """
    Kiểm tra tình trạng server
    """
    return {"status": "✅ Server is running", "version": "1.1.0"}
