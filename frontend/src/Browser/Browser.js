import React from "react";
import "./Browser.css";

function Browser({app}) {
    return (
        <div className="Browser">
            {app === "Home" && <h1>Home</h1>}
            {app === "Upload" && <h1>Upload</h1>}
        </div>
    );
}

export default Browser;