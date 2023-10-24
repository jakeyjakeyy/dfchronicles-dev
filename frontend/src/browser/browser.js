import React, {useState} from "react";
import "./browser.css";
import UploadXMLForm from "./upload/uploadxmlform";
import Worlds from "./worlds/worlds";
import World from "./world/world";

function Browser({app, onAppSelect}) {
    console.log(app);
    const [id, setId] = useState(null);

    const handleSelectId = (id) => {
        setId(id);
    }

    return (
        <div className="Browser">
            {app === "Home" && <h1>Home</h1>}
            {app === "Upload" && <UploadXMLForm />}
            {app === "Worlds" && <Worlds onAppSelect={onAppSelect} onSetId={handleSelectId} />}
            {app === "World" && <World id={id} onSetId={handleSelectId} onAppSelect={onAppSelect} />}
        </div>
    );
}

export default Browser;