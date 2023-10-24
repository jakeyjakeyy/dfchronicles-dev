import React from "react";
import "./world.css";
import LoadWorld from "../../utils/loadworld";
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

    if (!categoryData) {
        return (
            <div className="Category">
                <h3>Loading...</h3>
            </div>
        )
    }

    return (
        <div className="Category">
            <h3>{category}</h3>
            <ul>
                {categoryData.map((data) => (
                    <li key={data.id}>{data.name}</li>
                ))}
            </ul>
        </div>
    )
}

export default Category;