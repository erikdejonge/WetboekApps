//
//  SociaalrechtAppDelegate.m
//  Sociaalrecht
//
//  Created by rabshakeh on 9/17/09 - 12:29 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import "SociaalrechtAppDelegate.h"
#import "TableViewFromDatabaseViewController.h"
#import "ArtikelViewControllerFromXIB.h"
#import "WetboekSearchViewController.h"

@implementation SociaalrechtAppDelegate

@synthesize window;
@synthesize viewController;

-(void) applicationDidFinishLaunching: (UIApplication *) application
{
  TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init];

  tableViewFromDatabaseController.table_name = @"wetboekhoofdstuk";
  tableViewFromDatabaseController.next_table = @"wetboek";
  tableViewFromDatabaseController.title      = @"Sociaalrecht - Apr. 2011";
  [tableViewFromDatabaseController reload];
  navigationController = [[UINavigationController alloc] initWithRootViewController:tableViewFromDatabaseController];

  [tableViewFromDatabaseController release];
  navigationController.navigationBar.tintColor = [UIColor colorWithRed:0.46 green:0.06 blue:0.13 alpha:0];

  [window addSubview:[navigationController view]];

  [window makeKeyAndVisible];
}


-(void) dealloc
{
  [navigationController release];
  [viewController release];
  [window release];
  [super dealloc];
}


@end
