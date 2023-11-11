function loadHistoricalEvent(id, legendsxml, legendsplusxml) {
  var event = {};
  legendsxml.getElementsByTagName("historical_event").forEach((data) => {
    if (data.getElementsByTagName("id")[0].value === id) {
      event = data;
    }
  });
  return event;
}

export default loadHistoricalEvent;
