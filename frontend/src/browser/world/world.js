import React from "react";
import "./world.css";
import LoadWorld from "../../utils/loadworld";
import Category from "./category";
import { useState, useEffect } from "react";



function World({id, onSetId, onAppSelect}) {
    const [world, setWorld] = useState([]);
    const [category, setCategory] = useState("World");
    useEffect(() => {
        async function fetchData() {
            const world = await LoadWorld(id);
            setWorld(world);
        }
        fetchData();
    }, [id]);

    const handleClick = () => {
        if (category == "World") {
        onSetId(null);
        onAppSelect("Worlds");
        } else {
            setCategory("World");
        }
    }

    const handleCategory = (e) => {
        setCategory(e.target.innerHTML);
    }

    if (!world) {
        return (
            <div className="World">
                <h1>Loading...</h1>
            </div>
        )
    }

    const categories = ['Artifacts', 'Entities/Governments', 'Populations', 'Occasions', 'Historical Eras', 'Historical Event Collections', 'Historical Events', 'Historical Figures', 'Regions', 'Sites', 'Structures', 'Underground Regions', 'Written Contents', 'World Constructions', 'Music, Dance, Poetic forms', 'Landmasses', 'Mountain Peaks']
    // add dieties to categories

    return (
        <div className="World">
            <h1>{world.name2}</h1>
            <h2>{world.name}</h2>
            <button onClick={handleClick}>Back</button>
            {category == "World" &&
            <ul>
                {categories.map((category, index) => (
                    <li key={index} onClick={handleCategory}>{category}</li>
                ))}
            </ul>}
            {category != "World" && <Category category={category} world={world.id} />}
        </div>
    );
}

export default World;