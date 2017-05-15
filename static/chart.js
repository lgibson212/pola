var pubnub = new PubNub({
  publishKey: 'pub-c-616c5faf-bddc-4a94-8400-93dcfd6dc425',
  subscribeKey: 'sub-c-17eef582-38b5-11e7-a268-0619f8945a4f'
});
eon.chart({
  pubnub: pubnub,
  channels: ['eon-bar'],
  pubnub: pubnub,
  generate: {
    bindto: '#chart',
    data: {
      labels: true,
      type: 'bar'
    },
    bar: {
      width: {
        ratio: 0.5
      }
    },
    tooltip: {
        show: false
    }
  }
});

var pubnub1 = new PubNub({
  publishKey: 'pub-c-616c5faf-bddc-4a94-8400-93dcfd6dc425',
  subscribeKey: 'sub-c-17eef582-38b5-11e7-a268-0619f8945a4f'
});
setInterval(function(){

  pubnub1.publish({
    channel: channel,
    message: {
      eon: {
        'Austin': Math.floor(Math.random() * 99),
        'New York': Math.floor(Math.random() * 99),
        'San Francisco': Math.floor(Math.random() * 99),
        'Portland': Math.floor(Math.random() * 99)
      }
    }
  });

}, 1000);