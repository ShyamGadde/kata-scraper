var number = function(busStops){
  return busStops.reduce((people, inOut) => people += inOut[0] - inOut[1], 0);
}