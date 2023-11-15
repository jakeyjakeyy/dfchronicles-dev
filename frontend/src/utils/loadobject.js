import RefreshToken from "./refreshtoken";

function removeEmpty(obj) {
  for (const key in obj) {
    if (obj[key] === null || obj[key] === undefined || obj[key] === 0) {
      // Remove key if value is null or undefined
      delete obj[key];
    } else if (Array.isArray(obj[key]) && obj[key].length === 0) {
      // Remove key if value is an empty array
      delete obj[key];
    } else if (
      typeof obj[key] === "object" &&
      Object.keys(obj[key]).length === 0
    ) {
      // Remove key if value is an empty object
      delete obj[key];
    } else if (typeof obj[key] === "object") {
      // Call for all nested objects
      removeEmpty(obj[key]);
    }
  }
  return obj;
}

function LoadObj(id, category, object) {
  const token = localStorage.getItem("token");
  return fetch("http://localhost:8000/api/worlds", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `JWT ${token}`,
    },
    body: JSON.stringify({
      request: "world",
      id: id,
      category: category,
      object: object,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.message === "Invalid token" || data.code === "token_not_valid") {
        RefreshToken();
      } else {
        const world = JSON.parse(data);
        const cleanedWorld = removeEmpty(world);
        for (const key in cleanedWorld) {
          if (
            key === "event_collection" ||
            key === "attack_hf_historical_event_collections"
          ) {
            const promises = cleanedWorld[key].map((event) => {
              return LoadObj(id, "Historical Event Collections", event);
            });
            Promise.all(promises).then((eventCollections) => {
              cleanedWorld[key] = eventCollections;
              // return cleanedWorld;
            });
          }
          if (
            key === "hf_historical_events" ||
            key === "target_hf_historical_events"
          ) {
            const promises = cleanedWorld[key].map((event) => {
              return LoadObj(id, "Historical Events", event);
            });
            Promise.all(promises).then((events) => {
              cleanedWorld[key] = events;
              // return cleanedWorld;
            });
          }
        }
        return cleanedWorld;
      }
    })
    .catch((err) => {
      console.log(err);
    });
}

export default LoadObj;
