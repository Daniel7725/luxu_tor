#ifndef NULL
	#define NULL 0
#endif
#ifdef __cplusplus
extern "C"
{
#endif
#include "message.h"
#ifdef __cplusplus
}

static RegCallback reg_callback = NULL;

int device_register(struct reg_packet packet,RegCallback callback)
{
	reg_callback = callback;
	struct reg_response rep;
	rep.err = reg_response::SUCCESS;
	rep.user_id = "12345678";
	rep.user_token = "aaaaaaaaaaaaaaaa";
	callback(rep);
	return 0;
}
#endif
