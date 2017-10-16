#!/bin/bash -x

if [[ $MCMC_BUILDING_PAPER == false ]]; then
  return
fi

# Push to GitHub
if [ -n "$GITHUB_API_KEY" ]; then
  cd $TRAVIS_BUILD_DIR
  git checkout --orphan pdf
  git rm -rf .
  git add -f mcmc.pdf
  git -c user.name='travis' -c user.email='travis' commit -m "building the paper"
  git push -q -f https://dfm:$GITHUB_API_KEY@github.com/davidwhogg/mcmc pdf
fi
