import GetGen from "./getgen";

global.fetch = jest.fn();

describe("GetGen", () => {
  afterEach(() => {
    fetch.mockClear();
    localStorage.clear();
  });

  it("returns data on successful fetch", async () => {
    const mockResponse = { message: "Success" };
    fetch.mockResolvedValueOnce(new Response(JSON.stringify(mockResponse)));
    localStorage.setItem("token", "valid_token");
    const result = await GetGen({});
    expect(result).toEqual(mockResponse);
  });

  it("throws error on fetch failure", async () => {
    fetch.mockRejectedValueOnce(new Error("Fetch failed"));
    localStorage.setItem("token", "valid_token");
    await expect(GetGen({})).rejects.toThrow();
  });
});
