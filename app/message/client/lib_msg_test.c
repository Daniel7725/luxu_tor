#include "message.h"
#include <stdio.h>
static void reg_callback(struct reg_response rep)
{
	printf("err:%d\nuser_id:%s\nuser_token:%s\n",rep.err,rep.user_id,rep.user_token);
}
int main()
{
	struct reg_packet req = {"ios","bbbbbbbbbbbbbbbb","cccccccccccccccc","7.0.6","0.0.1"};
	int result = 0;
	result = device_register(req,reg_callback);
	return 0;
}
