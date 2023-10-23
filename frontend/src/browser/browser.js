import React from "react";
import "./browser.css";
import UploadXMLForm from "./upload/uploadxmlform";
import World from "./world/world";

function Browser({app}) {
    return (
        <div className="Browser">
            {app === "Home" && <h1>Home</h1>}
            {app === "Upload" && <UploadXMLForm />}
            {app === "Worlds" && <World />}
        </div>
    );
}

export default Browser;