#ifndef MESSAGE_H
#define MESSAGE_H
struct reg_packet
{
	const char *type;
	const char *token;
	const char *uuid;
	const char *sys_version;
	const char *soft_version;
}

struct reg_response
{
	enum Error
	{
		SUCCESS = 0,
		UNKNOWN_DEVICE = 1
	} err;
	const char *user_id;
	const char *user_token;
};

typedef void (*RegCallback)(struct reg_response response);
int device_register(struct reg_packet packet,RegCallback callback);

#endif
