import "./UploadCard.css";
import { useState } from "react";

const API_URL = "http://127.0.0.1:8000";

function UploadCard() {
    const [selectedFiles, setSelectedFiles] = useState([]);
    const [isDragging, setIsDragging] = useState(false);
    const [uploading, setUploading] = useState(false);
    const [uploaded, setUploaded] = useState(false);

    const uploadFiles = (files) => {

        setUploading(true);
        setUploaded(false);

        const formData = new FormData();

        files.forEach((file) => {
            formData.append("files", file);
        });

        fetch(`${API_URL}/upload`, {
            method: "POST",
            body: formData,
        })
            .then((response) => response.json())
            .then(() => {
                setUploading(false);
                setUploaded(true);
            })
            .catch((error) => {
                console.error(error);
                setUploading(false);
            });
    };

    const handleFileChange = (event) => {

        const files = Array.from(event.target.files);

        const pdfFiles = files.filter(
            (file) => file.type === "application/pdf"
        );

        if (pdfFiles.length === 0) return;

        setSelectedFiles(pdfFiles);

        uploadFiles(pdfFiles);
    };

    const handleDragOver = (event) => {
        event.preventDefault();
        setIsDragging(true);
    };

    const handleDragLeave = () => {
        setIsDragging(false);
    };

    const handleDrop = (event) => {
        event.preventDefault();
        setIsDragging(false);

        const files = Array.from(event.dataTransfer.files);

        const pdfFiles = files.filter(
            (file) => file.type === "application/pdf"
        );

        if (pdfFiles.length === 0) return;

        setSelectedFiles(pdfFiles);

        uploadFiles(pdfFiles);
    };

    return (
        <div
            className={`upload-card ${isDragging ? "dragging" : ""}`}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
        >
            <div className="upload-icon">📄</div>

            <h2>Upload your PDFs</h2>

            <p>Choose one or more research papers to compare.</p>

            <p className="small-text">
                Multiple PDF files are supported
            </p>

            <input
                id="pdfUpload"
                type="file"
                accept=".pdf"
                multiple
                onChange={handleFileChange}
                hidden
            />

            <label htmlFor="pdfUpload" className="upload-btn">
                📁 Choose PDFs
            </label>

            {uploading && (
                <p className="uploading">
                    Uploading PDFs...
                </p>
            )}

            {uploaded && (
                <>
                    {selectedFiles.map((file, index) => (
                        <p
                            key={index}
                            className="filename"
                        >
                            ✅ {file.name}
                        </p>
                    ))}

                    <p className="success-message">
                        PDFs uploaded successfully!
                    </p>
                </>
            )}
        </div>
    );
}

export default UploadCard;