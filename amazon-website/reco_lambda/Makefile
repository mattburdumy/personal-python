## Makefile for HelloLambda lambda

#
# HEY, HEY YOU! If you copied hello_lambda update these three variables before running make
#

FUNCTION=getSimilarProducts
SCRIPT=getSimilarProducts
DESCRIPTION="blergh"


build: clean
	mkdir .tmp
	cp *.py .tmp/
	cp -R python-libs/* .tmp/
	cp -R env .tmp/
	cd .tmp; zip -r ../lambda.zip ./*
	rm -rf .tmp

clean:
	rm -f lambda.zip
	rm -rf .tmp

create-lambda:
	aws lambda create-function --profile personal --function-name $(FUNCTION) --zip-file fileb://lambda.zip --role arn:aws:iam::636256167974:role/lambda_exec_role --handler $(SCRIPT).lambda_handler --runtime python2.7 --description $(DESCRIPTION)

#deploy-dev:
#	aws lambda update-function-code --profile dev --function-name $(FUNCTION) --zip-file fileb://lambda.zip

deploy:
	aws lambda update-function-code --profile personal --function-name $(FUNCTION) --zip-file fileb://lambda.zip

test:
	aws lambda invoke --profile personal  --invocation-type RequestResponse --function-name $(FUNCTION) --payload file://test-event.json /dev/stdout

#test:
#	aws s3 --profile prod cp test.csv s3://somebucket/somepath/

promote-prod: VERSION=$(shell aws lambda publish-version --profile default --function-name $(FUNCTION) | jq -r '.Version')
promote-prod:
	@echo Moving alias \"prod\" to version $(VERSION)
	aws lambda update-alias --profile prod --function-name $(FUNCTION) --function-version $(VERSION) --name PROD

tail:
	#cwtail --profile prod -sf /aws/lambda/$(FUNCTION)
	awslogs get /aws/lambda/$(FUNCTION) --profile default --watch

.PHONY : clean build
