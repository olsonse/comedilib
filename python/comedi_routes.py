#!/usr/bin/env python3
"""
Script to allow comedi device routing manipulation/queries on the command line.
"""

import argparse

import comedi

def list_routes(device, D, show_numeric):
  def _fmt_numeric(terminal):
    return '{} [{}]'.format(comedi.names.from_value[terminal], terminal)
  def _fmt_name_only(terminal):
    return '{}'.format(comedi.names.from_value[terminal])

  _fmt = _fmt_name_only
  if show_numeric:
    _fmt = _fmt_numeric

  n = comedi.get_routes(D, None, 0)
  print(device, 'has', n, 'routes')
  L = (comedi.route_pair*n)()
  n = comedi.get_routes(D, L, n)
  print('retrieved', n, 'routes')
  for r in L:
    t = test_route(D, r.source, r.destination)
    print(_fmt(r.source), '-->', _fmt(r.destination), '[{}]'.format(t),sep='\t')

def test_route(device, src, dest):
  if type(src) is not int:
    src = comedi.names.to_value[src]
  if type(dest) is not int:
    dest = comedi.names.to_value[dest]

  # -1 if not connectible
  # 0 if connectible but not connected
  # 1 if connectible and connected.
  ret = comedi.test_route(device, src, dest)
  if   ret == -1:
    return 'Not connectable'
  elif ret == 0:
    return 'Not connected'
  elif ret == 1:
    return 'Connected'

def connect_route(device, src, dest):
  if type(src) is not int:
    src = comedi.names.to_value[src]
  if type(dest) is not int:
    dest = comedi.names.to_value[dest]

  if comedi.connect_route(device, src, dest) < 0:
    src, dest = comedi.names.from_value[src], comedi.names.from_value[dest]
    raise RuntimeError('Could not connect route', src, '-->', dest)

def disconnect_route(device, src, dest):
  if type(src) is not int:
    src = comedi.names.to_value[src]
  if type(dest) is not int:
    dest = comedi.names.to_value[dest]

  if comedi.disconnect_route(device, src, dest) < 0:
    src, dest = comedi.names.from_value[src], comedi.names.from_value[dest]
    raise RuntimeError('Could not disconnect route', src, '-->', dest)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--device', required=True,
    help='Specify the comedi device to query/manipulate')
  parser.add_argument('-l', '--list', action='store_true',
    help='List all named routes for given device')
  parser.add_argument('-N', '--show-numeric', action='store_true',
    help='Show numeric values of sources and destinations')
  parser.add_argument('-t', '--test', nargs='*',
    help='Specify a series of space-separated routes to test as: src-dest')
  parser.add_argument('-C', '--connect', nargs='*',
    help='Specify a series of space-separated routes to connect as: src-dest')
  parser.add_argument('-D', '--disconnect', nargs='*',
    help='Specify a series of space-separated routes to disconnect as: src-dest')

  args = parser.parse_args()

  D = comedi.open(args.device)
  if not D:
    raise RuntimeError('Could not open device')

  try:
    if args.list:
      list_routes(args.device, D, args.show_numeric)

    if args.test:
      for l in args.test:
        src, dest = l.split('-')
        try: src = int(src)
        except: pass
        try: dest = int(dest)
        except: pass
        print(repr(src), '-->', repr(dest), ': ', test_route(D, src, dest))

    if args.connect:
      for l in args.connect:
        src, dest = l.split('-')
        try: src = int(src)
        except: pass
        try: dest = int(dest)
        except: pass
        print('Connecting: ', repr(src), '-->', repr(dest))
        connect_route(D, src, dest)

    if args.disconnect:
      for l in args.disconnect:
        src, dest = l.split('-')
        try: src = int(src)
        except: pass
        try: dest = int(dest)
        except: pass
        print('Disconnecting: ', repr(src), '-->', repr(dest))
        disconnect_route(D, src, dest)
  finally:
    comedi.close(D)


if __name__ == '__main__':
  main()
