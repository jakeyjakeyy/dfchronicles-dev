import React from "react";
import "./world.css";
import { useState, useEffect } from "react";
import GetGen from "../../utils/getgen";
import loadObjectClient from "../../utils/loadfromclient/loadobjectclient";

function Object({ object, legendsxml, legendsplusxml }) {
  const [response, setResponse] = useState([]);
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  console.log(legendsxml, legendsplusxml);

  useEffect(() => {
    async function fetchData() {
      console.log("loading");
      // Delay loading the object so loading screen can generate first
      setTimeout(() => {
        setData(
          loadObjectClient(object, setResponse, legendsxml, legendsplusxml)
        );
        setIsLoading(false);
      }, 1000);
    }
    fetchData();
  }, [object]);
  useEffect(() => {
    async function fetchData() {
      if (data.length === 0) {
        return;
      }
      console.log(data);
      const loadeddata = await GetGen(data);
      // const loadeddata = { generation: "test" };
      setResponse(loadeddata);
    }
    fetchData();
  }, [data]);

  if (isLoading) {
    return (
      <div className="Object">
        <h3>Gathering data...</h3>
      </div>
    );
  } else if (!response || response.length === 0) {
    return (
      <div className="Object">
        <h3>Generating chronicle...</h3>
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
      <div className="Object" style={{ whiteSpace: "pre-wrap" }}>
        <p>{response.generation}</p>
      </div>
    );
  }
}

export default Object;
