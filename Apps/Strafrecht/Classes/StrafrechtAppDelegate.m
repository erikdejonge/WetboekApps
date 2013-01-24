//
//  StrafrechtAppDelegate.m
//  Strafrecht
//
//  Created by rabshakeh on 8/18/09 - 3:54 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import "StrafrechtAppDelegate.h"
#import "TableViewFromDatabaseViewController.h"
#import "ArtikelViewControllerFromXIB.h"
#import "WetboekSearchViewController.h"

@implementation StrafrechtAppDelegate

@synthesize window;
@synthesize viewController;

-(void) applicationDidFinishLaunching: (UIApplication *) application
{
  TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init];

  tableViewFromDatabaseController.table_name = @"wetboekhoofdstuk";
  tableViewFromDatabaseController.next_table = @"wetboek";
  tableViewFromDatabaseController.title      = @"Strafrecht - Apr. 2011";
  [tableViewFromDatabaseController reload];
  navigationController = [[UINavigationController alloc] initWithRootViewController:tableViewFromDatabaseController];

  [tableViewFromDatabaseController release];
  navigationController.navigationBar.tintColor = [UIColor colorWithRed:0.015686274509803921 green:0.21176470588235294 blue:0.027450980392156862 alpha:0];

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
