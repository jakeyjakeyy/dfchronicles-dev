import React, { useState } from 'react';
import axios from 'axios';

function UploadXMLForm() {
    const [legends, setlegends] = useState(null);
    const [legendsplus, setlegendsplus] = useState(null);

    const handleFormSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('legends', legends);
        formData.append('legendsplus', legendsplus);

        try {
            await axios.post('http://localhost:8000/api/process-xml', formData);
            alert('XML files processed and data stored.');
        } catch (error) {
            console.error('Error processing XML files:', error);
        }
    };

    return (
        <form onSubmit={handleFormSubmit}>
            <input type="file" onChange={(e) => setlegends(e.target.files[0])} />
            <input type="file" onChange={(e) => setlegendsplus(e.target.files[0])} />
            <button type="submit">Upload and Process</button>
        </form>
    );
}

export default UploadXMLForm;
