import React from "react";
import "./worlds.css";
import { useState, useEffect } from "react";

function RefreshToken() {
  const refresh = localStorage.getItem("refresh");
  return fetch("http://localhost:8000/api/token/refresh", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ refresh: refresh }),
  })
    .then((res) => res.json())
    .then((data) => {
      localStorage.setItem("token", data.access);
    })
    .catch((err) => {
      console.log(err);
    });
}


function Worlds({onAppSelect, onSetId}) {
    const handleClick = (e) => {
        onSetId(e.target.id);
        onAppSelect("World");
    }
    const [worlds, setWorlds] = useState([]);
      
      async function GetWorlds() {
        const token = localStorage.getItem("token");
        const response = await fetch("http://localhost:8000/api/worlds", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `JWT ${token}`,
          },
          body: JSON.stringify({ request: "worlds" }),
        });
        const data = await response.json();
        if (data.message === "Invalid token" || data.code === "token_not_valid") {
            await RefreshToken();
            await GetWorlds();
            console.log("Refreshed token");
            window.location.reload();
            // return ("Refreshed token");
        } else {
          const worlds = JSON.parse(data);
          return worlds;
        }
      }

    useEffect(() => {
        async function fetchData() {
            const worlds = await GetWorlds();
            if (worlds === "Refreshed token") {
                setWorlds([]);
            } else {
            setWorlds(worlds);
            }
        }
        fetchData();
    }, []);

    return (
        <div className="World">
        <h3>Worlds</h3>
        <ul>
          {worlds.map((world) => (
            <li name={"World"} id={world.id} key={world.id} onClick={handleClick}>{world.name}</li>
          ))}
        </ul>
      </div>
    )
}
    

export default Worlds;