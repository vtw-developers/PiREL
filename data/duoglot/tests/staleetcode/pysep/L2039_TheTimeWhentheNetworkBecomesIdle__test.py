from L2039_TheTimeWhentheNetworkBecomesIdle import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1], [1, 2]], [0, 2, 1]]
    # output: 8
    # EXPLANATION:  At (the beginning of) second 0, - Data server 1 sends its message (denoted 1A) to the master server. - Data server 2 sends its message (denoted 2A) to the master server.  At second 1,  -   Message 1A arrives at the master server. Master server processes message 1A instantly and sends a reply 1A back. -   Server 1 has not received any reply. 1 second (1 < patience[1] = 2) elapsed since this server has sent the message, therefore it does not resend the message. -   Server 2 has not received any reply. 1 second (1 == patience[2] = 1) elapsed since this server has sent the message, therefore it resends the message (denoted 2B).  At second 2,  -   The reply 1A arrives at server 1. No more resending will occur from server 1. -   Message 2A arrives at the master server. Master server processes message 2A instantly and sends a reply 2A back. -   Server 2 resends the message (denoted 2C).     ...     At second 4, -   The reply 2A arrives at server 2. No more resending will occur from server 2.     ...     At second 7, reply 2D arrives at server 2.  Starting from the beginning of the second 8, there are no messages passing between servers or arriving at servers. This is the time when the network becomes idle.
    ,
    # example 2
    [[[0, 1], [0, 2], [1, 2]], [0, 10, 10]]
    # output: 3
    # EXPLANATION:  Data servers 1 and 2 receive a reply back at the beginning of second 2. From the beginning of the second 3, the network becomes idle.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
