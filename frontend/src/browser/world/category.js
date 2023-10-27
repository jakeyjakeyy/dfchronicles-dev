import React from "react";
import "./world.css";
import LoadWorld from "../../utils/loadworld";
import RefreshToken from "../../utils/refreshtoken";
import { useState, useEffect } from "react";

function Category({category, id}) {
    const [categoryData, setCategoryData] = useState([]);
    useEffect(() => {
        async function fetchData() {
            const categoryData = await LoadWorld(id, category);
            setCategoryData(categoryData);
        }
        fetchData();
    }, [id]);

    const fetchObj = e => {
        async function fetchData() {
            function LoadObj(id, category, object) {
            const token = localStorage.getItem("token");
            return fetch("http://localhost:8000/api/worlds", {
                method: "POST",
                headers: {
                "Content-Type": "application/json",
                Authorization: `JWT ${token}`,
                },
                body: JSON.stringify({ request: "world", id: id, category: category, object: object }),
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
            LoadObj(id, category, e.target.id);
        }
        fetchData();
    }

    if (!categoryData || categoryData.length === 0) {
        return (
            <div className="Category">
                <h3>Loading...</h3>
            </div>
        )
    }

    return (
        <div className="Category">
            <div className="CategoryTitle">
                <h3>{category}</h3>
            </div>
            <ul className="CategoryList">
                {categoryData.map((data) => (
                    <li key={data.id} category={category} id={data.id} onClick={fetchObj} >
                        {category === "Artifacts" && `${data.name} | ${data.item_type}`}
                        {category === "Entities/Governments" && `${data.race} ${data.type} | ${data.name}`}
                        {category === "Populations" && `${data.entity.name} | ${data.race} | ${data.population}`}
                        {category === "Occasions" && `${data.name}`}
                        {category === "Historical Eras" && `${data.name} | ${data.start_year} - ${data.end_year}`}
                        {category === "Historical Event Collections" && `${data.name} | ${data.type}`}
                        {category === "Historical Events" && `${data.type}`}
                        {category === "Historical Figures" && `${data.name} ${data.race} | ${data.birth_year}`}
                        {category === "Regions" && `${data.name} | ${data.type}`}
                        {category === "Sites" && `${data.name} | ${data.type}`}
                        {category === "Structures" && `${data.name} | ${data.type}`}
                        {category === "Underground Regions" && `${data.type} | ${data.depth}`}
                        {category === "Written Contents" && `${data.title} | ${data.form}`}
                        {category === "World Constructions" && `${data.name} | ${data.type}`}
                        {category === "Landmasses" && `${data.name} (${data.coord1})-(${data.coord2})`}
                        {category === "Mountain Peaks" && `${data.name} ${data.height} | ${data.volcano}`}
                        {category === "Plots" && `${data.type}`}
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Category;