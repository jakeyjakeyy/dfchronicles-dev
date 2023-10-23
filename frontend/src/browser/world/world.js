import React from "react";
import "./world.css";
import { useState, useEffect } from "react";


function World() {
    function RefreshToken() {
        const refresh = localStorage.getItem("refresh");
        fetch("http://localhost:8000/api/token/refresh", {
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
    function GetWorlds() {
        const token = localStorage.getItem("token");
        fetch("http://localhost:8000/api/worlds", {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            Authorization: `JWT ${token}`,
            },
            body: JSON.stringify({ request: "worlds" }),
        })
        .then((res) => res.json())
        .then((data) => {
            if (data.message === 'Invalid token'){
                RefreshToken();
                GetWorlds();
            }
        })
    }
    GetWorlds();
}
    

export default World;