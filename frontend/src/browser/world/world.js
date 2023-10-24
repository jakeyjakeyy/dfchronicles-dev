import React from "react";
import "./world.css";
import RefreshToken from "../../utils/refreshtoken";

function LoadWorld(id) {
    const token = localStorage.getItem("token");
    return fetch("http://localhost:8000/api/worlds", {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        Authorization: `JWT ${token}`,
      },
        body: JSON.stringify({ request: "world", id: id }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.message === "Invalid token" || data.code === "token_not_valid") {
          RefreshToken();
          LoadWorld(id);
        } else {
          const world = JSON.parse(data);
          return world;
        }
      })
      .catch((err) => {
        console.log(err);
      });
}

function World({id, onSetId, onAppSelect}) {
    LoadWorld(id)
    const handleClick = () => {
        onSetId(null);
        onAppSelect("Worlds");
    }

    return (
        <div className="World">
            <h1>World {id}</h1>
            <button onClick={handleClick}>Back</button>
        </div>
    );
}

export default World;