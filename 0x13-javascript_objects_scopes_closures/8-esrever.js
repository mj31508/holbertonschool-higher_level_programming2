#!/usr/bin/node

exports.esrever = function (list) {
  const store = [];
  for (let Nlength = list.length - (1); Nlength >= 0; Nlength--) {
    store.push(list[Nlength]);
  }
  return store;
}
