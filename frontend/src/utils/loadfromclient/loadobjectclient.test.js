import loadObjectClient from "./loadobjectclient";

describe("loadObjectClient", () => {
  it("returns empty if object undefined", () => {
    const input = undefined;
    const expectedOutput = {};

    const result = loadObjectClient(input, {}, {});

    expect(result).toEqual(expectedOutput);
  });
});

describe("loadObjectClient", () => {
  it("returns empty if object.name cant be matched", () => {
    const input = { name: "not a real object" };
    const expectedOutput = {};

    const result = loadObjectClient(input, {}, {});

    expect(result).toEqual(expectedOutput);
  });
});
