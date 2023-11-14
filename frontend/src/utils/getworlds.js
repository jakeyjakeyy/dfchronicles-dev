import RefreshToken from "./refreshtoken";

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
    await RefreshToken().then((res) => {
      if (res.message) {
        return res.message;
      }
    });
    await GetWorlds();
    console.log("Refreshed token");
    window.location.reload();
    // return ("Refreshed token");
  } else {
    const worlds = JSON.parse(data);
    return worlds;
  }
}

export default GetWorlds;
