import "./UploadCard.css";
import { useState } from "react";

function UploadCard() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [isDragging, setIsDragging] = useState(false);
    const [uploading, setUploading] = useState(false);
    const [uploaded, setUploaded] = useState(false);

    const handleFileChange = (event) => {
        const file = event.target.files[0];

        if (file && file.type === "application/pdf") {
            setSelectedFile(file);

            setUploading(true);
            setUploaded(false);

            setTimeout(() => {
                setUploading(false);
                setUploaded(true);
            }, 2500);
        }
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

        const file = event.dataTransfer.files[0];

        if (file && file.type === "application/pdf") {
            setSelectedFile(file);

            setUploading(true);
            setUploaded(false);

            setTimeout(() => {
                setUploading(false);
                setUploaded(true);
            }, 2500);
        }
    };

    return (
        <div
            className={`upload-card ${isDragging ? "dragging" : ""}`}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
        >
            <div className="upload-icon">📄</div>

            <h2>Upload your PDF</h2>

            <p>Choose a research paper or report to chat with.</p>

            <p className="small-text">
                Only PDF files are supported
            </p>

            <input
                id="pdfUpload"
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
                hidden
            />

            <label htmlFor="pdfUpload" className="upload-btn">
                📁 Choose PDF
            </label>

            {uploading && (
                <p className="uploading">
                    Uploading...
                </p>
            )}

            {uploaded && (
                <>
                    <p className="filename">
                        ✅ {selectedFile.name}
                    </p>

                    <p className="success-message">
                        PDF uploaded successfully!
                    </p>
                </>
            )}
        </div>
    );
}

export default UploadCard;
