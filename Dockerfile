#
#	MetaCall Telethon NodeJS Example by Parra Studios
#	Example of using Python Telethon in NodeJS with MetaCall.
#
#	Copyright (C) 2016 - 2020 Vicente Eduardo Ferrer Garcia <vic798@gmail.com>
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.
#

FROM alpine:latest

# Image descriptor
LABEL copyright.name="Vicente Eduardo Ferrer Garcia" \
	copyright.address="vic798@gmail.com" \
	maintainer.name="Vicente Eduardo Ferrer Garcia" \
	maintainer.address="vic798@gmail.com" \
	vendor="MetaCall Inc." \
	version="0.1"

# Install MetaCall
RUN apk add curl \
	&& curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh

COPY requirements.txt /

# Install Dependencies
RUN metacall pip3 install -r requirements.txt

# Copy sources
COPY index.js bot.py /

# # Run test
# RUN printf 'load py bot.py\ninspect\ncall run()\nexit' | metacall \
# 	&& cat /root/metacall.log

CMD [ "metacall", "index.js" ]