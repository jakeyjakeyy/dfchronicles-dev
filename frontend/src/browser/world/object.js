import React from "react";
import "./world.css";
import { useState, useEffect } from "react";
import GetGen from "../../utils/getgen";
import loadObjectClient from "../../utils/loadfromclient/loadobjectclient";

function Object({ object, legendsxml, legendsplusxml }) {
  const [response, setResponse] = useState([]);
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [status, setStatus] = useState("Loading");

  useEffect(() => {
    async function fetchData() {
      // Delay loading the object so loading screen can generate first
      setTimeout(async () => {
        const data = await loadObjectClient(
          object,
          legendsxml,
          legendsplusxml,
          setStatus
        );
        setData(data);
        setIsLoading(false);
      }, 1000);
    }
    fetchData();
  }, [object]);

  if (isLoading) {
    return (
      <div className="Object">
        <h4>Gathering data...</h4>
        <h5>{status}</h5>
      </div>
    );
  } else if (!response || response.length === 0) {
    async function fetchData() {
      if (data.length === 0) {
        return;
      }
      console.log(data);
      // const loadeddata = await GetGen(data);
      const loadeddata = { generation: "test" };
      setResponse(loadeddata);
    }
    fetchData();
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
