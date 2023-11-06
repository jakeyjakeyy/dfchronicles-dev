import React from "react";
import "./world.css";
import { useState, useEffect } from "react";
import GetGen from "../../utils/getgen";

function Object({ object }) {
  const [response, setResponse] = useState([]);
  useEffect(() => {
    async function fetchData() {
      if (object.length !== 0) {
        const response = await GetGen(object);
        // const response = "test";
        setResponse(response);
      }
    }
    fetchData();
  }, [object]);

  if (!response || response.length === 0) {
    return (
      <div className="Object">
        <h3>Loading...</h3>
      </div>
    );
  } else if (response.message) {
    return (
      <div className="Object">
        <h3>{response.message}</h3>
      </div>
    );
  } else {
    return (
      <div className="Object">
        <h3>{response}</h3>
      </div>
    );
  }
}

export default Object;
