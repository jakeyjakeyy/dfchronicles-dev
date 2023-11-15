import RefreshToken from "./refreshtoken";

async function GetGen(object) {
  const token = localStorage.getItem("token");
  const jsonobject = JSON.stringify(object);
  return fetch("http://localhost:8000/api/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `JWT ${token}`,
    },
    body: JSON.stringify({
      request: "generate",
      prompt: jsonobject,
    }),
  })
    .then((res) => res.json())
    .then(async (data) => {
      if (data.message === "Invalid token" || data.code === "token_not_valid") {
        const res = await RefreshToken();
        if (res && res.message === "Expired token") {
          return { message: "Please log in again." };
        }
        return GetGen(object);
      } else {
        return data;
      }
    })
    .catch((err) => {
      console.log(err);
      throw err;
    });
}

export default GetGen;
